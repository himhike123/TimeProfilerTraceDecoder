//
//  ViewController.swift
//  TimeProfiler
//
//  Created by Himanshi Gupta on 04/12/20.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        let mark = Person()
        let pancho = Dog()
        mark.dog = pancho
        pancho.owner = mark
    }


    
}

class Dog {
    var owner: Person?
}

class Person {
    var dog: Dog?
}
