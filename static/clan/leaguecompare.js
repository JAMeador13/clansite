function openLeftMenu() {
    document.getElementById("leftmenu").style.width = "25%";
    document.getElementById("leftmenu").style.display = "block";
}

function closeLeftMenu() {
    document.getElementById("leftmenu").style.display = "none";
}


function openTopLeft(evt, streamer) {
    var i, x, links;
    x = document.getElementsByClassName("topLeft");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    links = document.getElementsByClassName("topLeftBtn");
    for (i = 0; i < x.length; i++) {
        links[i].className = links[i].className.replace("w3-red", "w3-black");
    }
    document.getElementById(streamer).style.display = "block";
    evt.currentTarget.className = "w3-bar-item w3-button topLeftBtn w3-red";
}


function openBotLeft(evt, streamer) {
    var i, x, links;
    x = document.getElementsByClassName("botLeft");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    links = document.getElementsByClassName("botLeftBtn");
    for (i = 0; i < x.length; i++) {
        links[i].className = links[i].className.replace("w3-red", "w3-black");
    }
    document.getElementById(streamer).style.display = "block";
    evt.currentTarget.className = "w3-bar-item w3-button botLeftBtn w3-red";
}





function openRightMenu() {
    document.getElementById("rightmenu").style.width = "25%";
    document.getElementById("rightmenu").style.display = "block";
}

function closeRightMenu() {
    document.getElementById("rightmenu").style.display = "none";
}


function openTopRight(evt, streamer) {
    var i, x, links;
    x = document.getElementsByClassName("topRight");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    links = document.getElementsByClassName("topRightBtn");
    for (i = 0; i < x.length; i++) {
        links[i].className = links[i].className.replace("w3-red", "w3-black");
    }
    document.getElementById(streamer).style.display = "block";
    evt.currentTarget.className = "w3-bar-item w3-button topRightBtn w3-red";
}


function openBotRight(evt, streamer) {
    var i, x, links;
    x = document.getElementsByClassName("botRight");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    links = document.getElementsByClassName("botRightBtn");
    for (i = 0; i < x.length; i++) {
        links[i].className = links[i].className.replace("w3-red", "w3-black");
    }
    document.getElementById(streamer).style.display = "block";
    evt.currentTarget.className = "w3-bar-item w3-button botRightBtn w3-red";
}