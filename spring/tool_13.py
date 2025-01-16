import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def main():
    print("Number Info (Lookup)")

    try:
        phone_number = input("Enter phone number (e.g., +33123456789): ")
        print("Processing...")

        parsed_number = phonenumbers.parse(phone_number, None)
        if phonenumbers.is_valid_number(parsed_number):
            if phone_number.startswith("+"):
                country_code = "+" + phone_number[1:3] 
            else:
                country_code = "None"

            operator = carrier.name_for_number(parsed_number, "fr")
            type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
            timezones = timezone.time_zones_for_number(parsed_number)
            timezone_info = timezones[0] if timezones else None
            country = phonenumbers.region_code_for_number(parsed_number)
            region = geocoder.description_for_number(parsed_number, "fr")
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
            status = "Valid"
        else:
            formatted_number = "None"
            region = "None"
            country = "None"
            operator = "None"
            type_number = "None"
            timezone_info = "None"
            country_code = "None"
            status = "Invalid"

        print(f"""
        Phone         : {phone_number}
        Formatted     : {formatted_number}
        Status        : {status}
        Country Code  : {country_code}
        Country       : {country}
        Region        : {region}
        Timezone      : {timezone_info}
        Operator      : {operator}
        Type Number   : {type_number}
        """)

    except phonenumbers.phonenumberutil.NumberParseException:
        print("Invalid phone number format! Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
