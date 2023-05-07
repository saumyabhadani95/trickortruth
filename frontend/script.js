async function fetchData() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200){
            record = JSON.parse(xmlHttp.responseText);
            headline_list = record.posts;
            console.log(headline_list);
            headline_list_display = ""
            for (var i=0;i<headline_list.length;i++)
                headline_list_display = headline_list_display + "<li>"+ headline_list[i].title + "</li>"
            //document.getElementById("concerts").innerHTML = record.posts.map(item => `<li>${item.title}</li>`).join('');
            document.getElementById("headlines").innerHTML = headline_list_display;
        }
    }
    xmlHttp.open("GET", 'http://127.0.0.1:5000/getjson', true);
    xmlHttp.send(null);
}

function radioclicked() {
    console.log("Is something printing???");
    var misleading_list = document.getElementById('misleading_ul').getElementsByTagName('li');
    var misleading_bool = false;
    for (var i = 0; i< misleading_list.length; i++) {
        var radio_element = misleading_list[i].getElementsByTagName('input');
        if (radio_element[0].checked == true)
            misleading_bool = true;
    }

    var biased_list = document.getElementById('biased_ul').getElementsByTagName('li');
    var biased_bool = false;
    for (var i = 0; i< biased_list.length; i++) {
        var radio_element = biased_list[i].getElementsByTagName('input');
        if (radio_element[0].checked == true)
            biased_bool = true;
    }

    var clear_list = document.getElementById('clear_ul').getElementsByTagName('li');
    var clear_bool = false;
    for (var i = 0; i< clear_list.length; i++) {
        var radio_element = clear_list[i].getElementsByTagName('input');
        if (radio_element[0].checked == true)
            clear_bool = true;
    }

    if (misleading_bool && biased_bool && clear_bool)
        document.getElementById("submitbutton").disabled = false;

}

function submitclicked() {
    document.getElementById("survey").visibility = "hidden";
    document.getElementById("message").visibility = "visible";
    let url = "";
    chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
        url = tabs[0].url;
        console.log(url);
        // use `url` here inside the callback because it's asynchronous!
    })
}

function clearscales() {
    var elements = document.getElementsByTagName("input");

    for (var i = 0; i < elements.length; i++) {
        if (elements[i].type == "radio")
            elements[i].checked = false;
    }

    document.getElementById("submitbutton").disabled = true;
}

/*
function onWindowLoad() {
    var message = document.querySelector('#message');

    chrome.tabs.query({ active: true, currentWindow: true }).then(function (tabs) {
        var activeTab = tabs[0];
        var activeTabId = activeTab.id;

        return chrome.scripting.executeScript({
            target: { tabId: activeTabId },
            // injectImmediately: true,  // uncomment this to make it execute straight away, other wise it will wait for document_idle
            func: DOMtoString,
            // args: ['body']  // you can use this to target what element to get the html for
        });

    }).then(function (results) {
        var htmlpage = results[0].result;
        const parser = new DOMParser();
        const htmlDoc = parser.parseFromString(htmlpage, 'text/html');
        //var el = document.createElement( 'html' );
        //el.innerHTML = htmlpage;
        var metaelements = htmlDoc.getElementsByTagName( 'meta' );
        for(var i=0;i<metaelements.length;i++){
            if(metaelements[i].getAttribute("property") == 'og:title'){
                console.log(metaelements[i].getAttribute("content"));
                //document.getElementById("headline").innerHTML = metaelements[i].getAttribute("content");
            }
        }
        //console.log(htmlpage);
        //var xmlHttp = new XMLHttpRequest();
        //xmlHttp.onreadystatechange = function() {
        //    if (xmlHttp.readyState == 4 && xmlHttp.status == 200){
        //        record = JSON.parse(xmlHttp.responseText);
        //        headline = record.title;
        //        document.getElementById("headlines").innerHTML = headline;
        //    }
        //}
        //console.log("Here????")
        //xmlHttp.open("GET", 'http://127.0.0.1:5000/parseHTML?htmlpage='+htmlpage, true);
        //xmlHttp.send(null);            
    }).catch(function (error) {
        message.innerText = 'There was an error injecting script : \n' + error.message;
    });
}*/

//window.onload = onWindowLoad;

/*function DOMtoString(selector) {
    if (selector) {
        selector = document.querySelector(selector);
        if (!selector) return "ERROR: querySelector failed to find node"
    } else {
        selector = document.documentElement;
    }
    return selector.outerHTML;
}*/

document.getElementById("clearbutton").addEventListener("click", clearscales);
document.getElementById("submitbutton").addEventListener("click", submitclicked);
document.getElementById("misleading_strong_agree").addEventListener("click", radioclicked);
document.getElementById("misleading_agree").addEventListener("click", radioclicked);
document.getElementById("misleading_neutral").addEventListener("click", radioclicked);
document.getElementById("misleading_disagree").addEventListener("click", radioclicked);
document.getElementById("misleading_strong_disagree").addEventListener("click", radioclicked);
document.getElementById("biased_strong_agree").addEventListener("click", radioclicked);
document.getElementById("biased_agree").addEventListener("click", radioclicked);
document.getElementById("biased_neutral").addEventListener("click", radioclicked);
document.getElementById("biased_disagree").addEventListener("click", radioclicked);
document.getElementById("biased_strong_disagree").addEventListener("click", radioclicked);
document.getElementById("clear_strong_agree").addEventListener("click", radioclicked);
document.getElementById("clear_agree").addEventListener("click", radioclicked);
document.getElementById("clear_neutral").addEventListener("click", radioclicked);
document.getElementById("clear_disagree").addEventListener("click", radioclicked);
document.getElementById("clear_strong_disagree").addEventListener("click", radioclicked);

//onWindowLoad(); 