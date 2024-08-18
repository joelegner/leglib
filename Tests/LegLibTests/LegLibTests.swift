@testable import LegLib
import XCTest

final class LegLib: XCTestCase {
    func testEmail() throws {
        let email = try Email("john.appleseed@apple.com")
        XCTAssertEqual(email.description, "john.appleseed@apple.com")
        
        XCTAssertThrowsError(try Email("invalid"))
    }
}

class SigDigTests: XCTestCase {
    
    func testSmallNumber() {
        let result = SigDig(3.14159)
        XCTAssertEqual(result, "3.14")
    }
    
    func testSmallNumberWithLeadingZeros() {
        let result = SigDig(0.00123456)
        XCTAssertEqual(result, "0.00123")
    }
    
    func testLargerNumber() {
        let result = SigDig(123.456)
        XCTAssertEqual(result, "123")
    }

    func testThousandsNumber() {
        let result = SigDig(43124.32111)
        XCTAssertEqual(result, "43,100")
    }
    
    func testVeryLargeNumber() {
        let result = SigDig(987654.321)
        XCTAssertEqual(result, "988,000")
    }
    
    func testSmallNumberWithMoreLeadingZeros() {
        let result = SigDig(0.000987654)
        XCTAssertEqual(result, "0.000988")
    }
}
