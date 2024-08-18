import Foundation

struct Email: CustomStringConvertible {
    var description: String
    
    public init(_ emailString: String) throws {
        let regex = #"[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,64}"#
        guard let _ = emailString.range(of: regex, options: .regularExpression) else {
            throw InvalidEmailError(email: emailString)
        }
        self.description = emailString
    }
}

private struct InvalidEmailError: Error {
    let email: String
}

public func SigDig(_ number: Double) -> String {
    let formatter = NumberFormatter()
    formatter.numberStyle = .decimal
    formatter.maximumSignificantDigits = 3
    formatter.usesSignificantDigits = true
    
    if let roundedString = formatter.string(for: number) {
        return roundedString
    }
    return "\(number)"
}
