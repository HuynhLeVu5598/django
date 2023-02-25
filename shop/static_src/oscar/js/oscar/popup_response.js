(function () {
  "use strict";
  var initData = JSON.parse(document.getElementById("shop-popup-response-constants").dataset.popupResponse);
  switch (initData.action) {
    case "change":
      window.opener.shop.dismissChangeRelatedObjectPopup(window, initData.value, initData.obj, initData.new_value);
      break;
    case "delete":
      window.opener.shop.dismissDeleteRelatedObjectPopup(window, initData.value);
      break;
    default:
      window.opener.shop.dismissAddRelatedObjectPopup(window, initData.value, initData.obj);
      break;
  }
})();
