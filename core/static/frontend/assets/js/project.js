const asterisk_img = document.querySelector(".asterisk-img");
const categories = document.querySelectorAll("#pills-home-tab");

function addAsterisk(target) {
  console.log(categories[0].children[0].children[0].children[2].children[1]);
  console.log(target);
  for (let i = 0; i < categories.length; i++) {
    if (
      target === categories[i] &&
      categories[i].children[0].children[0].children[2].children[1].children
        .length === 0
    ) {
      var tag = document.createElement("img");
      tag.src = "/static/frontend/assets/images/star_1.png";
      categories[i].children[0].children[0].children[2].children[1].appendChild(
        tag
      );
    }

    if (
      target == categories[i] &&
      categories[i].children[0].children[0].children[2].children[1].children
        .length === 1
    ) {
    } else {
      categories[i].children[0].children[0].children[2].children[1].innerHTML =
        "";
    }
  }
}
