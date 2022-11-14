const popupBtn = document.querySelector(".similarBtn");
const closePopup = document.querySelector(".closePopup");
const greyOut = document.querySelector(".availableSelections");
const popup = document.querySelector(".available");

popupBtn.addEventListener("click", function () {
  popup.style.display = "block";
  popup.style.zIndex = "2";
  greyOut.style.display = "block";
  greyOut.style.backgroundColor = "black";
  greyOut.style.opacity = "0.5";
  greyOut.style.positon = "fixed";
  greyOut.style.zIndex = "1";
  //   greyOut.style.zIndex = "1";
  //   greyOut.style.zIndex = "1";
});

closePopup.addEventListener("click", () => {
  popup.style.display = "none";
  greyOut.style.display = "none";
});
