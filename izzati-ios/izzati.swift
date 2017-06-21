import Foundation

class Izzati {
  var url = "http://192.168.100.118:5020/"

  func send(text: [String: AnyObject] = nil, file: UIImage = nil) -> [String: AnyObject] {
    var request = URLRequest(url: URL(string: url)!)
    request.httpMethod = "POST"
    if text != nil & file != nil {
      if let theJSONData = try? JSONSerialization.data(
        withJSONObject: text,
        options: []) {
        let theJSONText = String(data: theJSONData, encoding: .ascii)
      }
      let param = [
          "json"  : theJSONText
      ]
      let imageData = UIImageJPEGRepresentation(data!, 1)
      if(imageData==nil)  { return; }
      request.HTTPBody = createBodyWithParameters(param, filePathKey: "file", imageDataKey: imageData!, boundary: boundary)
      let task = NSURLSession.sharedSession().dataTaskWithRequest(request) {
          data, response, error in

          if error != nil {
              print("error=\(error)")
              return
          }
      do {
          let jsonDic = NSJSONSerialization.JSONObjectWithData(jsonData, options: NSJSONReadingOptions.MutableContainers, error: &error) as Dictionary<String, AnyObject>;

          return jsonDic

      }catch
      {
          print(error)
      }
    }
      task.resume()

    } else if text != nil {
      if let theJSONData = try? JSONSerialization.data(
        withJSONObject: text,
        options: []) {
        let theJSONText = String(data: theJSONData, encoding: .ascii)
      }
      let param = [
          "json"  : theJSONText
      ]
      request.HTTPBody = createBodyWithParameters(param, boundary: boundary)
      let task = NSURLSession.sharedSession().dataTaskWithRequest(request) {
          data, response, error in

          if error != nil {
              print("error=\(error)")
              return
          }
      do {
          let jsonDic = NSJSONSerialization.JSONObjectWithData(jsonData, options: NSJSONReadingOptions.MutableContainers, error: &error) as Dictionary<String, AnyObject>;

          return jsonDic

      }catch
      {
          print(error)
      }
    }
      task.resume()
    } else if data != nil {
      let imageData = UIImageJPEGRepresentation(data!, 1)
      if(imageData==nil)  { return; }
      request.HTTPBody = createBodyWithParameters(filePathKey: "file", imageDataKey: imageData!, boundary: boundary)
      let task = NSURLSession.sharedSession().dataTaskWithRequest(request) {
          data, response, error in

          if error != nil {
              print("error=\(error)")
              return
          }
      do {
          let jsonDic = NSJSONSerialization.JSONObjectWithData(jsonData, options: NSJSONReadingOptions.MutableContainers, error: &error) as Dictionary<String, AnyObject>;

          return jsonDic

      }catch
      {
          print(error)
      }
    }
      task.resume()
    } else {
      return
    }
  }


  func createBodyWithParameters(parameters: [String: String]?, filePathKey: String?, imageDataKey: NSData = nil, boundary: String) -> NSData {
    let body = NSMutableData();

    if parameters != nil {
        for (key, value) in parameters! {
            body.appendString("--\(boundary)\r\n")
            body.appendString("Content-Disposition: form-data; name=\"\(key)\"\r\n\r\n")
            body.appendString("\(value)\r\n")
        }
    }

    if imageDataKey != nil {
      let filename = "image.jpg"
      let mimetype = "image/jpg"

      body.appendString("--\(boundary)\r\n")
      body.appendString("Content-Disposition: form-data; name=\"\(filePathKey!)\"; filename=\"\(filename)\"\r\n")
      body.appendString("Content-Type: \(mimetype)\r\n\r\n")
      body.appendData(imageDataKey)
      body.appendString("\r\n")
    }

    body.appendString("--\(boundary)--\r\n")

    return body
  }



  func generateBoundaryString() -> String {
      return "Boundary-\(NSUUID().UUIDString)"
  }


}
extension NSMutableData {

    func appendString(string: String) {
        let data = string.dataUsingEncoding(NSUTF8StringEncoding, allowLossyConversion: true)
        appendData(data!)
    }
}
