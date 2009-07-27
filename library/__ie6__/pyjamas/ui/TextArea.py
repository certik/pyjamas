class TextArea:
    def getCursorPos(self):
        JS("""
        try {
            var elem = this.getElement();
            var tr = elem.document.selection.createRange();
            var tr2 = tr.duplicate();
            tr2.moveToElementText(elem);
            tr.setEndPoint('EndToStart', tr2);
            tr_text = tr.text;
            var select_text = tr_text;
            if (tr.compareEndPoints("StartToEnd", tr) == 0)
                return select_text.length;
            tr.moveEnd("character", -1);
            while (tr.text == tr_text) {
                select_text += "\\r\\n";
                if (tr.compareEndPoints("StartToEnd", tr) == 0)
                    return select_text.length;
                tr.moveEnd("character", -1);
            }
            return select_text.length;
        }
        catch (e) {
            return 0;
        }
        """)


