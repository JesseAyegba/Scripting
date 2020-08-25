$(document).ready(function() {
    var $body = $("body");
    var $home = $("#home");
    var $about = $("#about");
    var $services = $("#services");
    var $contact = $("#contact");
    var $root = $(".root");

    

    $home.on("click", function() {
        var res = new XMLHttpRequest();
        res.open("GET", "https://www.jromtech.com");
        res.onload = function() {
            var response = res.responseText
            $root.html(response);
        }
        res.send(); 
    });
    $about.on("click", function() {
        var res = new XMLHttpRequest();
        res.open("GET", "https://www.jromtech.com/about");
        res.onload = function() {
            var response = res.responseText
            $root.html(response);
        }
        res.send(); 
    });

    $services.on("click", function() {
        var res = new XMLHttpRequest();
        res.open("GET", "https://www.jromtech.com/services");
        res.onload = function() {
            var response = res.responseText
            $root.html(response);
        }
        res.send(); 
    });

    $contact.on("click", function() {
        var res = new XMLHttpRequest();
        res.open("GET", "https://www.jromtech.com/contact");
        res.onload = function() {
            var response = res.responseText
            $root.html(response);
        }
        res.send(); 
    });


    
});