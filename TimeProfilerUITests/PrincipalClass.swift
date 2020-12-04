//
//  PrincipalClass.swift
//  MemoryLeaksUITests
//
//  Created by Himanshi Gupta on 17/11/20.
//  Copyright © 2020 Himanshi Gupta. All rights reserved.
//

import Foundation
import XCTest

class PrincipalClass: NSObject, XCTestObservation {
    override init() {
        super.init()
        XCTestObservationCenter.shared.addTestObserver(self)
    }
}
