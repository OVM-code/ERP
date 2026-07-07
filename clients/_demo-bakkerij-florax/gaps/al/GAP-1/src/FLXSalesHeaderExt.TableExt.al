tableextension 50101 "FLX Sales Header Ext" extends "Sales Header"
{
    fields
    {
        field(50100; "FLX Origin"; Enum "FLX Order Origin")
        {
            Caption = 'Origin', Comment = 'NL="Herkomst"';
            Editable = false;
            DataClassification = CustomerContent;
        }
    }
}

enum 50100 "FLX Order Origin"
{
    Extensible = true;
    value(0; " ") { Caption = ' ', Locked = true; }
    value(1; WEBSHOP) { Caption = 'Webshop', Comment = 'NL="Webshop"'; }
    value(2; EDI) { Caption = 'EDI', Locked = true; }
}
