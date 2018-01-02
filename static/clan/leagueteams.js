function openTeam(evt, teamName) {
    var i, x, teamtabs;
    x = document.getElementsByClassName("team");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    teamtabs = document.getElementsByClassName("teamtab");
    for (i = 0; i < x.length; i++) {
        teamtabs[i].className = teamtabs[i].className.replace("w3-red", "w3-black");
    }
    document.getElementById(teamName).style.display = "block";
    evt.currentTarget.className = "w3-bar-item w3-button w3-red teamtab";
}
