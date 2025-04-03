function showsharedialog(noteid){
    if (noteid == null || noteid == undefined || noteid == "") {
        console.error("Note ID is null or undefined.");
        alert("please save the note first.");
        return;
    }
    let share_dialog = new ShareDialog(noteid);
    document.body.appendChild(share_dialog.getElement());
}