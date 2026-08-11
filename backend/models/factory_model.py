class FactoryModel:

    def __init__(
        self,
        factory_id=None,
        factory_name=None,
        industry=None,
        registration_number=None,
        address=None,
        city=None,
        state=None,
        country="India",
        pincode=None,
        contact_phone=None,
        time_zone="Asia/Kolkata"
    ):

        self.factory_id = factory_id
        self.factory_name = factory_name
        self.industry = industry
        self.registration_number = registration_number
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.pincode = pincode
        self.contact_phone = contact_phone
        self.time_zone = time_zone