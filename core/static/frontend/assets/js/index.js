const more_info = document.querySelector(".more-info");
// const more_info_less_info = document.querySelector(".more-info-less-info");

const less_info = document.querySelector(".less-info");

const email_linkedin_instagram_tabs = document.querySelector(
  ".email-linkedin-instagram-tabs"
);

more_info.onclick = (e) => {
  more_info.classList.add("active-border");
  // less_info.classList.remove("active-border");
  email_linkedin_instagram_tabs.style.position = "relative";
  email_linkedin_instagram_tabs.style.display = "block";
  email_linkedin_instagram_tabs.style.height = "200px";

  less_info.style.display = "block";
};

// less_info.onclick = () => {
//   more_info.classList.remove("active-border");
//   less_info.classList.add("active-border");
//   email_linkedin_instagram_tabs.style.display = "none";
//   email_linkedin_instagram_tabs.style.height = "0px";

//   less_info.style.display = "none";
// };

function checkHoveredElement(element) {
  const currentElement = element?.getAttribute("id");
  const relevantImg = document.querySelector(`.${currentElement}`);
  console.log(relevantImg);
  if (relevantImg?.classList?.contains("display-none")) {
    relevantImg?.classList?.remove("display-none");
  }
}

function hideCurrentElImg(element) {
  const currentElement = element?.getAttribute("id");
  const relevantImg = document.querySelector(`.${currentElement}`);
  console.log(relevantImg);
  if (!relevantImg?.classList?.contains("display-none")) {
    relevantImg?.classList?.add("display-none");
  }
}
