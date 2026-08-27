(function () {
  const storageKey = "cece-ai-notes:tutorial-tag";

  function normalizedPath(value) {
    const path = new URL(value, window.location.href).pathname;
    return path.endsWith("/") ? path : `${path}/`;
  }

  function findTutorialItem(anchor, tutorialPath) {
    return normalizedPath(anchor.href).endsWith(`/${tutorialPath}`);
  }

  function createButton(label, count) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "tutorial-tag-filter__button";
    button.dataset.tag = label;
    button.setAttribute("aria-pressed", "false");
    button.append(document.createTextNode(label));
    if (count !== undefined) {
      const counter = document.createElement("span");
      counter.textContent = String(count);
      button.append(counter);
    }
    return button;
  }

  function mountFilter(data) {
    const sidebar = document.querySelector(".md-sidebar--primary .md-sidebar__scrollwrap");
    if (!sidebar || sidebar.querySelector(".tutorial-tag-filter")) return;

    const anchors = Array.from(sidebar.querySelectorAll("a.md-nav__link"));
    const tutorialItems = data.tutorials.map((tutorial) => ({
      ...tutorial,
      element: anchors.find((anchor) => findTutorialItem(anchor, tutorial.path))?.closest(".md-nav__item"),
    })).filter((tutorial) => tutorial.element);
    if (!tutorialItems.length) return;

    const filter = document.createElement("section");
    filter.className = "tutorial-tag-filter";
    filter.setAttribute("aria-label", "按标签筛选教程");

    const title = document.createElement("p");
    title.className = "tutorial-tag-filter__title";
    title.textContent = "按标签筛选";

    const controls = document.createElement("div");
    controls.className = "tutorial-tag-filter__controls";
    controls.append(createButton("全部", tutorialItems.length));
    data.tags.forEach((tag) => {
      const count = tutorialItems.filter((tutorial) => tutorial.tags.includes(tag)).length;
      controls.append(createButton(tag, count));
    });
    filter.append(title, controls);
    const tutorialNav = tutorialItems[0].element.closest("nav.md-nav");
    (tutorialNav || sidebar).append(filter);

    function applyTag(tag) {
      const selected = tag === "全部" || data.tags.includes(tag) ? tag : "全部";
      filter.querySelectorAll("button").forEach((button) => {
        button.setAttribute("aria-pressed", String(button.dataset.tag === selected));
      });
      tutorialItems.forEach((tutorial) => {
        tutorial.element.hidden = selected !== "全部" && !tutorial.tags.includes(selected);
      });
      window.sessionStorage.setItem(storageKey, selected);
    }

    controls.addEventListener("click", (event) => {
      const button = event.target.closest("button[data-tag]");
      if (button) applyTag(button.dataset.tag);
    });
    applyTag(window.sessionStorage.getItem(storageKey) || "全部");
  }

  const script = Array.from(document.scripts).find((item) => item.src.includes("tag-filter.js"));
  if (!script) return;
  const dataUrl = new URL("../assets/tutorial-tags.json", script.src);
  fetch(dataUrl)
    .then((response) => response.ok ? response.json() : Promise.reject())
    .then(mountFilter)
    .catch(() => {});
}());
