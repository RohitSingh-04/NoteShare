class SaveDialog{

    constructor(){
        this.component = document.createElement("div");
        this.component.className = "save-dialog";
        this.createForm();
        this.component.id = "save-dialog";
    }

    createForm(){
        // save form
        let saveform = document.createElement("form");
        saveform.className = "save-form";
        saveform.id = "save-form";
        saveform.method = "POST";
        saveform.action = "/save/";

        saveform.appendChild(this.createSaveInput());
        saveform.appendChild(this.createSaveButton());
        saveform.appendChild(this.createCsrfToken());
        saveform.appendChild(this.createCloseButton());
        saveform.appendChild(this.createContent());

        this.component.appendChild(saveform);
    }

    createSaveInput(){
        // inputbox
        let nameinputbox = document.createElement("input");
        nameinputbox.type = "text";
        nameinputbox.placeholder = "Enter a name for your note";
        nameinputbox.className = "name-input-box";
        nameinputbox.id = "name-input-box";
        nameinputbox.name = "title";
        nameinputbox.required = true;

        return nameinputbox;
    }

    createSaveButton(){
        let savebutton = document.createElement("input");
        savebutton.type = "submit";
        savebutton.innerText = "Save";
        savebutton.className = "save-button";
        savebutton.id = "save-button";
        return savebutton;
    }

    createCsrfToken(){
        let csrf_token = document.createElement("input");
        csrf_token.type = "hidden";
        csrf_token.name = "csrfmiddlewaretoken";
        csrf_token.value = document.querySelector("[name=csrfmiddlewaretoken]").value;
        return csrf_token;
    }

    createCloseButton(){
        let closebutton = document.createElement("button");
        closebutton.innerText = "Close";
        closebutton.className = "close-button";
        closebutton.id = "close-button";
        closebutton.onclick = function(){
            document.getElementById("save-dialog").remove();
        }
        return closebutton;
    }

    createContent(){
        let content = document.getElementById("editor");
        let contentbox = document.createElement("input");
        contentbox.type = "hidden";
        contentbox.name = "content";
        contentbox.value = content.value;
        return contentbox;
    }

    createSharableCheckbox(){
        let checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.name = "sharable";
        checkbox.id = "sharable-checkbox";
        checkbox.value = "true";

        let label = document.createElement("label");
        label.innerText = "Make this note sharable";
        label.setAttribute("for", "sharable-checkbox");

        let container = document.createElement("div");
        container.appendChild(checkbox);
        container.appendChild(label);

        return container;
    }

    getElement(){
        return this.component;
    }

}