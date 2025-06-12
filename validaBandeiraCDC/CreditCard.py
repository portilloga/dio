import re

class CreditCard:
    def validateFlag(self, card_number: str) -> dict:
        card_number = card_number.strip()
        if not card_number.isdigit():
            return {
                "cardNumber": card_number,
                "isValid": False,
                "message": "invalid credit card number"
            }

        # List all valid lengths for all flags
        valid_lengths = [13, 14, 15, 16, 19]
        if len(card_number) not in valid_lengths:
            return {
                "cardNumber": card_number,
                "isValid": False,
                "message": "invalid credit card number"
            }

        rules = [
            {
                "flag": "Visa",
                "regex": r"^4\d{12}(\d{3})?(\d{3})?$",
                "lengths": [13, 16, 19]
            },
            {
                "flag": "Mastercard",
                "regex": r"^(5[1-5]\d{14}|2(2(2[1-9]\d{12}|[3-9]\d{13})|[3-6]\d{14}|7([01]\d{13}|20\d{12})))$",
                "lengths": [16]
            },
            {
                "flag": "American Express",
                "regex": r"^3[47]\d{13}$",
                "lengths": [15]
            },
            {
                "flag": "Hipercard",
                "regex": r"^(3841(0|40|60)\d{10}|606282\d{10}|637095\d{8}|637568\d{8}|637599\d{8}|637609\d{8}|637612\d{8})$",
                "lengths": [14, 16]
            },
            {
                "flag": "Diners International",
                "regex": r"^3[689]\d{12}$",
                "lengths": [14]
            },
            {
                "flag": "Elo",
                "regex": r"^(4011(78|79)\d{10}|431274\d{10}|438935\d{10}|451416\d{10}|457393\d{10}|4576(31|32)\d{10}|504175\d{10}|506(699|7[0-6]\d|77[0-8])\d{10}|509\d{13}|627780\d{10}|636297\d{10}|636368\d{10}|6500(31|32|33)\d{10}|6500(35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51)\d{10}|6504(05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39)\d{10}|6504(85|86|87|88|89|90|91|92|93|94|95|96|97|98)\d{10}|6505(41|42|43|44|45|46|47|48|49|50|51|52|53|54|55|56|57|58)\d{10}|6507(00|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18)\d{10}|6507(20|21|22|23|24|25|26|27)\d{10}|6509(01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18)\d{10}|6516(52|53|54|55|56|57|58|59|60|61|62|63|64|65|66|67|68|69|70|71|72|73|74|75|76|77|78|79)\d{10}|6550(00|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19)\d{10}|6550(21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|53|54|55|56|57|58)\d{10})$",
                "lengths": [16]
            }
        ]


        for rule in rules:
            if len(card_number) in rule["lengths"] and re.match(rule["regex"], card_number):
                return {
                    "cardNumber": card_number,
                    "isValid": True,
                    "message": f"credit card flag: {rule['flag']}"
                }

        return {
            "cardNumber": card_number,
            "isValid": False,
            "message": "Inexistent credit card flag"
        }