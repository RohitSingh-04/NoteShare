class ShareDialog{
    constructor(id){
        this.component = document.createElement("div");
        this.component.className = "share-dialog";
        this.createForm(id);
        this.component.id = "share-dialog";
    }

    createForm(noteid){
        // share form
        let shareform = document.createElement("form");
        shareform.className = "share-form";
        shareform.id = "share-form";
        shareform.method = "POST";
        shareform.action = `/share/${noteid}`;

        shareform.appendChild(this.createCsrfToken());
        shareform.appendChild(this.createUsernameInputFeild());
        shareform.appendChild(this.createShareButton());
        shareform.appendChild(this.createCloseButton());
        this.component.appendChild(shareform);
    }

    createUsernameInputFeild(){
        let userNameInput = document.createElement("input");
        userNameInput.type = "text";
        userNameInput.name = "user_name";
        userNameInput.placeholder = "User Name";
        userNameInput.className = "user-name-input";
        userNameInput.id = "user-name-input";
        userNameInput.required = true;
        return userNameInput;
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
            document.getElementById("share-dialog").remove();
        }
        return closebutton;
    }

    createShareButton(){
        let sharebutton = document.createElement("input");
        sharebutton.type = "submit";
        sharebutton.innerText = "Share";
        sharebutton.className = "share-button";
        sharebutton.id = "share-button";
        return sharebutton;
    }

    getElement(){
        return this.component;
    }

}