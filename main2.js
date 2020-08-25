var root = document.querySelector(".root");
var some = document.querySelectorAll(".something");
var foo = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]



some.forEach((item) => {
    item.addEventListener("mouseover", () => {
        item.classList.add("make-big");
    });
    item.addEventListener("mouseout", () => {
        item.classList.remove("make-big");
    });
});  

class Student {
    constructor(name, surname) {
        this.name = name;
        this.surname = surname;
    }
    correctWay() {
        
    }
}

var jesse = new Student("Jesse", "Ayegba");
jesse.correctWay()