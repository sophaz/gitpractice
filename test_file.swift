class Profile: Object, FetchOrCreatable {

    typealias T = Profile

    @NSManaged var name: String
    @NSManaged var streetAddress: String
    @NSManaged var city: String
    @NSManaged var likedShops: Set<Shop>?

    static var currentProfile: Profile?

    override func parse(_ data: [String : Any]) {
        super.parse(data)

        if let dataDict = data["data"] as? [String: Any] {
            if let name = dataDict["name"] as? String {
                self.name = name
            }
            if let address = dataDict["street_address"] as? String {
                self.streetAddress = address
            }
            if let city = dataDict["city"] as? String {
                self.city = city
            }
        }
    }

    func makeDict() -> [String: Any] {
        var dict: [String: Any] = [:]

        dict["name"] = self.name
        dict["street_address"] = self.streetAddress
        dict["city"] = self.city

        return dict
    }

}

