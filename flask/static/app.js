function openChatWindow(){
  document.getElementById("chat-form-container").style.display = "block";
}
function closeChatWindow(){
  document.getElementById("chat-form-container").style.display = "none";
}

$(function () {
  var ChatDiv = $('.chat_container');
  var height = ChatDiv[0].scrollHeight;
  ChatDiv.scrollTop(height);
});