
function showRecommendations() {
    const searchInput = document.getElementById("searchInput");
    const genreFilter = document.getElementById("genreFilter");
    const movieList = document.getElementById("movieList");
    const message = document.getElementById("noResults");

    // Stop if the catalogue filters aren't on this page.
    if (!searchInput || !genreFilter || !movieList) {
        return;
    }

    const search = searchInput.value.trim().toLowerCase();
    const genre = genreFilter.value;
    const cards = movieList.querySelectorAll(".movie-card");
    let visibleCount = 0;

    cards.forEach(card => {
        const title = (card.dataset.title || "").toLowerCase();
        const movieGenre = card.dataset.genre || "";

        const matchesSearch = title.includes(search);
        const matchesGenre = genre === "All" || movieGenre === genre;
        const visible = matchesSearch && matchesGenre;

        card.style.display = visible ? "" : "none";

        if (visible) {
            visibleCount++;
        }
    });

    if (message) {
        message.textContent = visibleCount === 0
            ? "No movies found. Try another search."
            : "";

        message.style.display = visibleCount === 0 ? "block" : "none";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("searchInput");
    const genreFilter = document.getElementById("genreFilter");

    if (searchInput) {
        searchInput.addEventListener("input", showRecommendations);
    }

    if (genreFilter) {
        genreFilter.addEventListener("change", showRecommendations);
    }

    showRecommendations();
});

// Interactive movie wheel: uses the currently loaded catalogue, no external API required.
document.addEventListener("DOMContentLoaded", () => {
    const wheel = document.getElementById("movieWheel");
    const spinButton = document.getElementById("spinWheel");
    const genreSelect = document.getElementById("wheelGenre");
    const result = document.getElementById("wheelResult");
    const movieLink = document.getElementById("wheelMovieLink");
    if (!wheel || !spinButton) return;

    let rotation = 0;
    spinButton.addEventListener("click", () => {
        const cards = Array.from(document.querySelectorAll("#movieList .movie-card"));
        const genre = genreSelect ? genreSelect.value : "All";
        const candidates = cards.filter(card =>
            card.dataset.title &&
            (genre === "All" || card.dataset.genre === genre) &&
            card.style.display !== "none"
        );
        if (!candidates.length) {
            result.textContent = "No movies match this category yet. Add movies to your catalogue or choose another genre.";
            movieLink.hidden = true;
            return;
        }
        spinButton.disabled = true;
        movieLink.hidden = true;
        result.textContent = "The wheel is spinning...";
        const chosen = candidates[Math.floor(Math.random() * candidates.length)];
        const title = chosen.querySelector("h3")?.textContent?.trim() || chosen.dataset.title;
        const href = chosen.querySelector(".movie-link")?.getAttribute("href") || "#";
        const segment = 360 / candidates.length;
        const target = Math.floor(Math.random() * candidates.length);
        rotation += 1440 + (360 - ((rotation + target * segment) % 360));
        wheel.style.transform = `rotate(${rotation}deg)`;
        window.setTimeout(() => {
            result.textContent = `Tonight's pick: ${title}`;
            movieLink.href = href;
            movieLink.hidden = false;
            spinButton.disabled = false;
        }, 4100);
    });
});
