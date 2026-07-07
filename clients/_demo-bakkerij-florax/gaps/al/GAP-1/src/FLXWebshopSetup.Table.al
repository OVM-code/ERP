table 50100 "FLX Webshop Setup"
{
    Caption = 'Webshop Setup', Locked = false;
    DataClassification = CustomerContent;

    fields
    {
        field(1; "Primary Key"; Code[10]) { Caption = 'Primary Key'; }
        field(10; "Stock Feed Endpoint"; Text[250])
        {
            Caption = 'Stock Feed Endpoint', Comment = 'NL="Voorraadfeed-endpoint"';
            // TODO(TGD §6.2): API key in isolated storage, set from the page — never stored here.
        }
        field(11; "Location Filter"; Code[10])
        {
            Caption = 'Location Filter', Comment = 'NL="Vestigingsfilter"';
            TableRelation = Location;
        }
        field(12; "Feed Enabled"; Boolean) { Caption = 'Feed Enabled', Comment = 'NL="Feed actief"'; }
        field(13; "QC Blocked Statuses"; Text[100])
        {
            Caption = 'QC Blocked Lot Statuses', Comment = 'NL="QC-geblokkeerde lotstatussen"';
            // TGD §8: Aptean status values are configuration — never hardcode (GEBLOKKEERD-QC;AFGEKEURD at go-live).
        }
    }
    keys { key(PK; "Primary Key") { Clustered = true; } }
}
