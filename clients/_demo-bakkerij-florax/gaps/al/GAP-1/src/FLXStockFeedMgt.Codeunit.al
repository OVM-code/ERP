codeunit 50111 "FLX Stock Feed Mgt"
{
    // Sellable-stock feed (TGD §5, outbound). Runs from job queue codeunit 50112 every 15 min.

    procedure BuildAndSendFeed()
    var
        Setup: Record "FLX Webshop Setup";
        Item: Record Item;
    begin
        Setup.Get();
        if not Setup."Feed Enabled" then
            exit;
        Item.SetRange(Blocked, false);
        // TODO(TGD §5): filter to items with a webshop SKU (framework translation table, A4).
        if Item.FindSet() then
            repeat
                // sellable := inventory(location) − QC-blocked lot qty − reserved qty.
                // Lots blocked ONLY by the retail shelf-life rule DO count (AC-3).
                AddLine(Item."No.", SellableQty(Item, Setup));
            until Item.Next() = 0;
        // TODO(TGD §5): hand dataset to framework outbound message WEBSHOP-STOCK
        // (retry/notification = framework outbox config, 3 retries — AC-5).
    end;

    local procedure SellableQty(Item: Record Item; Setup: Record "FLX Webshop Setup"): Decimal
    begin
        // TODO(TGD §5): Item.CalcFields(Inventory) with Location Filter;
        // subtract lot entries whose Aptean status is in Setup."QC Blocked Statuses";
        // subtract "Reserved Qty. on Inventory". Test T-3 fixture: 1200/200/150/100 → 850.
        exit(0);
    end;

    local procedure AddLine(ItemNo: Code[20]; Qty: Decimal)
    begin
        // TODO(TGD §5): {itemNo, sku, sellableQty, timestamp} into the outbound buffer.
    end;
}
