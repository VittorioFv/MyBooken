document.getElementById('bodybkg').style.display = 'none';
const toggle = document.getElementById('toggle');
const sidebar = document.getElementById('sidebar');
const toggletoken = document.getElementById('toggletoken');
const sidebartoken = document.getElementById('sidebartoken');

document.getElementById('bodybkg').onclick = function (e) {
    toggletoken.classList.remove('active');
    sidebartoken.classList.remove('active');
    toggle.classList.remove('active');
    sidebar.classList.remove('active');
    document.getElementById('bodybkg').style.display = 'none';
}

toggle.onclick = function () {
    toggle.classList.add('active');
    sidebar.classList.add('active');
    document.getElementById('bodybkg').style.display = 'block';
    toggletoken.classList.remove('active');
    sidebartoken.classList.remove('active');

}

toggletoken.onclick = function () {
    toggletoken.classList.add('active');
    sidebartoken.classList.add('active');
    document.getElementById('bodybkg').style.display = 'block';
    toggle.classList.remove('active');
    sidebar.classList.remove('active');
}
