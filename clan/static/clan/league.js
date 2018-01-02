function openThreeTeam(evt, teamName) {
    var i, x, teamtabs;
    x = document.getElementsByClassName("s3team");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    teamtabs = document.getElementsByClassName("s3teamtab");
    for (i = 0; i < x.length; i++) {
        teamtabs[i].className = teamtabs[i].className.replace("w3-red", "w3-black");
    }
    document.getElementById(teamName).style.display = "block";
    evt.currentTarget.className = "w3-bar-item w3-button s3teamtab w3-red";
}


function openOneTab(evt, tabName) {
    var i, x, linktabs;
    x = document.getElementsByClassName("s1subTab");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    linktabs = document.getElementsByClassName("s1linktab");
    for (i = 0; i < x.length; i++) {
        linktabs[i].className = linktabs[i].className.replace("w3-red", "w3-black");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className = "w3-bar-item w3-button s1linktab w3-red";
}

function openTwoTab(evt, tabName) {
    var i, x, linktabs;
    x = document.getElementsByClassName("s2subTab");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    linktabs = document.getElementsByClassName("s2linktab");
    for (i = 0; i < x.length; i++) {
        linktabs[i].className = linktabs[i].className.replace("w3-red", "w3-black");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className = "w3-bar-item w3-button s2linktab w3-red";
}

function openThreeTab(evt, tabName) {
    var i, x, linktabs;
    x = document.getElementsByClassName("s3subTab");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    linktabs = document.getElementsByClassName("s3linktab");
    for (i = 0; i < x.length; i++) {
        linktabs[i].className = linktabs[i].className.replace("w3-red", "w3-black");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className = "w3-bar-item w3-button s3linktab w3-red";
}


function openSeason(evt, seasonNum) {
    var i, x, tablinks;
    x = document.getElementsByClassName("season");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace("w3-red", "w3-black");
    }
    document.getElementById(seasonNum).style.display = "block";
    evt.currentTarget.className = "w3-bar-item w3-button tablink w3-red";
}


function openLeftMenuThree() {
    document.getElementById("s3leftMenu").style.width = "15%";
    document.getElementById("s3leftMenu").style.display = "block";
}

function closeLeftMenuThree() {
    document.getElementById("s3leftMenu").style.display = "none";
}

function openLeftTeamThree(evt, teamName) {
    var i, x, teamlinks;
    x = document.getElementsByClassName("s3leftteamcard");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    teamlinks = document.getElementsByClassName("s3leftteambutton");
    for (i = 0; i < x.length; i++) {
        teamlinks[i].className = teamlinks[i].className.replace("w3-red", "w3-black");
    }
    document.getElementById(teamName).style.display = "block";
    evt.currentTarget.className = "w3-bar-item w3-button s3leftteambutton w3-red";
}




function openRightMenuThree() {
    document.getElementById("s3rightMenu").style.width = "15%";
    document.getElementById("s3rightMenu").style.display = "block";
}

function closeRightMenuThree() {
    document.getElementById("s3rightMenu").style.display = "none";
}

function openRightTeamThree(evt, teamName) {
    var i, x, teamlinks;
    x = document.getElementsByClassName("s3rightteamcard");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    teamlinks = document.getElementsByClassName("s3rightteambutton");
    for (i = 0; i < x.length; i++) {
        teamlinks[i].className = teamlinks[i].className.replace("w3-red", "w3-black");
    }
    document.getElementById(teamName).style.display = "block";
    evt.currentTarget.className = "w3-bar-item w3-button s3rightteambutton w3-red";
}
