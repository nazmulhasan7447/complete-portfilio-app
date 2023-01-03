const asterisk_img = document.querySelector(".asterisk-img");
const categories = document.querySelectorAll("#pills-home-tab");

function addAsterisk(target) {
  for (let i = 0; i < categories.length; i++) {
    if (
      target === categories[i] &&
      categories[i].children[0].children[1].children[1].children.length === 0
    ) {
      var tag = document.createElement("img");
      tag.src = "./assets/images/star_1.png";
      categories[i].children[0].children[1].children[1].appendChild(tag);
    }
    if (
      target === categories[i] &&
      categories[i].children[0].children[1].children[1].children.length === 1
    ) {
    } else {
      categories[i].children[0].children[1].children[1].innerHTML = "";
    }
  }
}
