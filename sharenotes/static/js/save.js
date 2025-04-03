function show_save_dialog(notename, note_id){
    let save_dialog = new SaveDialog();
    document.body.appendChild(save_dialog.getElement());
    if (notename){
        document.getElementById("name-input-box").value = notename;
        document.getElementById("save-form").action = `/update/${note_id}/`;
        document.getElementById("save-button").value = "Update";
    }
}