import Foundation

func jssGetDeviceInfo(deviceID: String, completion: @escaping (String) -> Void) {
    let username: String = "api_user"
    let password: String = "jamf1234"
    let jssRealm = "Restful JSS Access -- Please supply your credentials"
    let credential = URLCredential(user: username, password: password, persistence: URLCredential.Persistence.forSession)
    let protectionSpace = URLProtectionSpace(host: "127.0.0.1", port: 8080, protocol: "http", realm: jssRealm, authenticationMethod: NSURLAuthenticationMethodHTTPBasic)
    URLCredentialStorage.shared.setDefaultCredential(credential, for: protectionSpace)
    let config = URLSessionConfiguration.default
    config.httpAdditionalHeaders = [
        "Content-Type": "text/xml",
        //"Accept": "application/xml",
        //"Accept": "application/json"
    ]
    let session = URLSession(configuration: config)
    let jssAddress = "http://127.0.0.1:8080"
    let apiAddress: String = "/JSSResource/mobiledevices/id/"
    let jssEndpoint: String = jssAddress + apiAddress + deviceID
    let url = URL(string: jssEndpoint)!
    let task = session.dataTask(with: url) { (data, response, error)  in
        if let data = data,
            let string = String(data: data, encoding: .utf8) {
            print(string)
            completion(string)
        }
    }
    task.resume()
}

jssGetDeviceInfo(deviceID: "26") { (deviceInfo) in
    print("Success")
}
