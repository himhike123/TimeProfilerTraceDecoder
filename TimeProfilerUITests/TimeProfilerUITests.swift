//
//  TimeProfilerUITests.swift
//  TimeProfilerUITests
//
//  Created by Himanshi Gupta on 04/12/20.
//

import XCTest

class TimeProfilerUITests: XCTestCase {

    override func setUpWithError() throws {
        // Put setup code here. This method is called before the invocation of each test method in the class.
        XCUIApplication().launch()
        sleep(12)
        // In UI tests it is usually best to stop immediately when a failure occurs.
        continueAfterFailure = false

        // In UI tests it’s important to set the initial state - such as interface orientation - required for your tests before they run. The setUp method is a good place to do this.
    }

    override func tearDownWithError() throws {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }

    func testExample() throws {
        // UI tests must launch the application that they test.
        let app = XCUIApplication()
        for _ in 1...4 {
            app.launch()
            sleep(5)
            app.tap()
            sleep(2)
            XCTAssert(app.exists)
        }
    }

    func testExample4() throws {
        // UI tests must launch the application that they test.
        let app = XCUIApplication()
        for _ in 1...4 {
            app.launch()
            sleep(5)
            app.tap()
            sleep(2)
            XCTAssert(app.exists)
        }
    }
}
