codeunit 50110 "FLX Webshop Order Mgt"
{
    // Inbound post-processing for framework message WEBSHOP-ORDER (TGD §5, inbound).

    var
        DuplicateOrderErr: Label 'DUPLICATE_ORDER: a sales order with external document no. %1 already exists for customer %2.',
            Comment = 'NL="DUPLICATE_ORDER: er bestaat al een verkooporder met extern documentnr. %1 voor klant %2."';

    // VERIFY: exact publisher/event against the installed framework version (TGD §5 / A3).
    // Expected: codeunit "CGK Inbox Dispatcher", event OnAfterCreateDocument(MessageCode, RecRef, InboxTransaction).
    // [EventSubscriber(ObjectType::Codeunit, Codeunit::"CGK Inbox Dispatcher", 'OnAfterCreateDocument', '', true, true)]
    procedure OnAfterCreateWebshopOrder(var SalesHeader: Record "Sales Header" /* ; var InboxTransaction: Record ... */)
    begin
        SalesHeader."FLX Origin" := SalesHeader."FLX Origin"::WEBSHOP;
        SalesHeader.Modify(true);

        if HasDuplicate(SalesHeader) then begin
            // TODO(TGD §5.2): raise framework inbox error DuplicateOrderErr, then delete this order (AC-4).
            Error(DuplicateOrderErr, SalesHeader."External Document No.", SalesHeader."Sell-to Customer No.");
        end;

        AdjustRequestedDeliveryDate(SalesHeader); // TGD §5.3 / FGD §3.3 (14:00 rule, company calendar)
        // TGD §5.4: no bypass of standard validation — validation errors must surface as inbox errors.
    end;

    local procedure HasDuplicate(SalesHeader: Record "Sales Header"): Boolean
    var
        Other: Record "Sales Header";
    begin
        Other.SetRange("Document Type", Other."Document Type"::Order);
        Other.SetRange("Sell-to Customer No.", SalesHeader."Sell-to Customer No.");
        Other.SetRange("External Document No.", SalesHeader."External Document No.");
        Other.SetFilter("No.", '<>%1', SalesHeader."No.");
        exit(not Other.IsEmpty());
    end;

    local procedure AdjustRequestedDeliveryDate(var SalesHeader: Record "Sales Header")
    begin
        // TODO(TGD §5.3): if Time >= 14:00 and Requested Delivery Date < tomorrow,
        // set to next working day via the company base calendar.
    end;
}
