// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

function customMailtoUrl() {
  if (window.localStorage == null)
    return "";
  if (window.localStorage.customMailtoUrl == null)
    return "";
  return window.localStorage.customMailtoUrl;
}

function defaultBreadCrumbsEndpoint() {
    var defaultURL = "http://adelpozo.xyz/breadcrumbs";

    if (window.localStorage != null && window.localStorage.breadCrumbsServerURL != null)
        return window.localStorage.breadCrumbsServerURL;

    return defaultURL;
}

function sendToServerold(tab_id, subject, body, selection) {
  var url = "http://127.0.0.1:5000/";
  var representationOfDesiredState = "The cheese is old and moldy, where is the bathroom?";

  var client = new XMLHttpRequest();
  client.open("PUT", url, false);
  client.setRequestHeader("Content-Type", "text/plain");
  client.send(representationOfDesiredState);

  if (client.status == 200)
      alert("The request succeeded!\n\nThe response representation was:\n\n" + client.responseText)
  else
      alert("The request did not succeed!\n\nThe response status was: " + client.status + " " + client.statusText + ".");  
}

function sendToServer(tab_id, subject, body, selection) {
  alert("sendToServer")
  var url = defaultBreadCrumbsEndpoint()+"/addmore";
  
  var client = new XMLHttpRequest();
  client.open("POST", url, false);
  client.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  client.send("param2="+body);

  if (client.status == 200)
      alert("The request succeeded!\n\nThe response representation was:\n\n" + client.responseText)
  else
      alert("The request did not succeed!\n\nThe response status was: " + client.status + " " + client.statusText + ".");  
}

function executeMailto(tab_id, subject, body, selection) {
  var default_handler = customMailtoUrl().length == 0;

  var action_url = "mailto:?"
      if (subject.length > 0)
        action_url += "subject=" + encodeURIComponent(subject) + "&";

  if (body.length > 0) {
    action_url += "body=" + encodeURIComponent(body);

    // Append the current selection to the end of the text message.
    if (selection.length > 0) {
      action_url += encodeURIComponent("\n\n") +
          encodeURIComponent(selection);
    }
  }

  if (!default_handler) {
    // Custom URL's (such as opening mailto in Gmail tab) should have a
    // separate tab to avoid clobbering the page you are on.
    var custom_url = customMailtoUrl();
    action_url = custom_url.replace("%s", encodeURIComponent(action_url));
    console.log('Custom url: ' + action_url);
    chrome.tabs.create({ url: action_url });
  } else {
    // Plain vanilla mailto links open up in the same tab to prevent
    // blank tabs being left behind.
    console.log('Action url: ' + action_url);
    chrome.tabs.update(tab_id, { url: action_url });
  }
}

chrome.runtime.onConnect.addListener(function(port) {
  var tab = port.sender.tab;

  // This will get called by the content script we execute in
  // the tab as a result of the user pressing the browser action.
  port.onMessage.addListener(function(info) {
    var max_length = 1024;
    if (info.selection.length > max_length)
      info.selection = info.selection.substring(0, max_length);
    sendToServer(tab.id, info.title, tab.url, info.selection);
  });
});

// Called when the user clicks on the browser action icon.
chrome.browserAction.onClicked.addListener(function(tab) {
  // We can only inject scripts to find the title on pages loaded with http
  // and https so for all other pages, we don't ask for the title.
  if (tab.url.indexOf("http:") != 0 &&
      tab.url.indexOf("https:") != 0) {
    sendToServer(tab.id, "", tab.url, "");
  } else {
    chrome.tabs.executeScript(null, {file: "content_script.js"});
  }
});
