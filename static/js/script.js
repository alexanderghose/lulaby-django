const selectedOptions = { taille: [], marque: [], etat: [], couleur: [], prix: [], matiere: [], trier: [] };

function updateTags(category) {
  const tagContainer = document.querySelector(`.${category}-tags`);
  const countSpan = document.querySelector(`.${category}-menu .dropdown-header span`);
  tagContainer.innerHTML = '';

  selectedOptions[category].forEach(option => {
    const tag = document.createElement('span');
    tag.classList.add('selected-tag');
    tag.innerHTML = `${option} <span class="remove-tag" onclick="removeTag('${category}', '${option}')">×</span>`;
    tagContainer.appendChild(tag);
  });

  countSpan.textContent = `${selectedOptions[category].length} sélectionné(s)`;
}

function selectOption(category, option) {
  if (!selectedOptions[category].includes(option)) {
    if (category === 'trier') {
      resetCategory('trier')
    }
    selectedOptions[category].push(option);
    updateTags(category);
  }
}

function removeTag(category, option) {
  selectedOptions[category] = selectedOptions[category].filter(item => item !== option);
  updateTags(category);
}

function resetCategory(category) {
  selectedOptions[category] = [];
  updateTags(category);
}

// Toggle dropdown visibility
function toggleDropdown(category) {
  // Close all dropdowns first
  document.querySelectorAll('.dropdown').forEach(dropdown => {
    if (!dropdown.classList.contains(category)) {
      dropdown.classList.remove('active');
    }
  });

  // Toggle the clicked dropdown
  document.querySelector(`.${category}`).classList.toggle("active");
}

// ✅ NEW: Close dropdown when clicking outside
document.addEventListener('click', function (event) {
  const isDropdown = event.target.closest('.dropdown');

  if (!isDropdown) {
    document.querySelectorAll('.dropdown').forEach(dropdown => {
      dropdown.classList.remove('active');
    });
  }
});

// ✅ FIXED updatePrice FUNCTION
function updatePrice() {
  let minPrice = parseInt(document.getElementById("min-price").value, 10);
  let maxPrice = parseInt(document.getElementById("max-price").value, 10);

  if (minPrice > maxPrice) [minPrice, maxPrice] = [maxPrice, minPrice];

  document.getElementById("price-label").textContent = `${minPrice}€ - ${maxPrice}€`;

  selectedOptions['prix'] = [`${minPrice}€ - ${maxPrice}€`]; // Store price range in tags
  updateTags('prix');
}

function resetAllFilters() {
  Object.keys(selectedOptions).forEach(category => {
    selectedOptions[category] = [];
    updateTags(category);
  });

  // Reset price range sliders
  document.getElementById("min-price").value = 0;
  document.getElementById("max-price").value = 500;
  document.getElementById("price-label").textContent = "0€ - 500€";
}



// ✅ photos
document.getElementById("photoInput").addEventListener("change", function (event) {
  const photoContainer = document.getElementById("photoContainer");
  const addPhotoBox = document.getElementById("addPhotoBox");
  const files = event.target.files;

  let currentPhotos = photoContainer.querySelectorAll(".photo-box:not(#addPhotoBox)").length;
  const maxPhotos = 10;

  for (let i = 0; i < files.length; i++) {
    if (currentPhotos >= maxPhotos) {
      break; // Stopper l'ajout si on atteint la limite
    }

    const file = files[i];
    const reader = new FileReader();

    reader.onload = function (e) {
      // Créer une div pour l'image
      const photoDiv = document.createElement("div");
      photoDiv.classList.add("photo-box");

      // Ajouter l'image
      const img = document.createElement("img");
      img.src = e.target.result;
      img.classList.add("photo-preview");

      // Ajouter le bouton supprimer
      const removeBtn = document.createElement("button");
      removeBtn.innerHTML = "❌";
      removeBtn.classList.add("remove-photo");
      removeBtn.style.color = "black"; // Assure que la croix est noire
      removeBtn.onclick = function () {
        photoContainer.removeChild(photoDiv);
        updatePhotoLimit();
      };

      // Ajouter les éléments dans la div
      photoDiv.appendChild(img);
      photoDiv.appendChild(removeBtn);
      photoContainer.insertBefore(photoDiv, addPhotoBox);

      currentPhotos++;
      updatePhotoLimit();
    };

    reader.readAsDataURL(file);
  }
});

// Fonction pour masquer/afficher le bouton d'ajout
function updatePhotoLimit() {
  const photoContainer = document.getElementById("photoContainer");
  const addPhotoBox = document.getElementById("addPhotoBox");
  const photoCount = photoContainer.querySelectorAll(".photo-box:not(#addPhotoBox)").length;

  if (photoCount >= 10) {
    addPhotoBox.style.display = "none";
  } else {
    addPhotoBox.style.display = "flex";
  }
}

//✅ marque
document.getElementById('marque').addEventListener('keydown', function (event) {
  if (event.key === 'Enter') {
    event.preventDefault();
  }
});


//✅ prix
function validatePrice(input) {
  // Supprime tout ce qui n'est pas un chiffre ou un point
  input.value = input.value.replace(/[^0-9.]/g, '');

  // Vérifie qu'il n'y a pas plus d'un point
  let parts = input.value.split('.');
  if (parts.length > 2) {
    input.value = parts[0] + '.' + parts.slice(1).join('');
  }

  // Limite à 2 décimales après le point
  if (parts.length === 2 && parts[1].length > 2) {
    input.value = parts[0] + '.' + parts[1].substring(0, 2);
  }

  // Vérifie la plage (0 - 500 euros)
  let price = parseFloat(input.value);
  if (isNaN(price) || price < 0 || price > 500) {
    input.value = "";
    alert("Le prix doit être un nombre compris entre 0 et 500 euros.");
  }
}


//✅ matiere
function toggleMatiereInput() {


  let matiereSelect = document.getElementById("matiere");
  let matiereAutre = document.getElementById("matiereAutre");

  if (matiereSelect.value === "autre") {
    matiereAutre.style.display = "inline-block";
    matiereAutre.focus();
  } else {
    matiereAutre.style.display = "none";
    matiereAutre.value = "";
  }
}

//✅ partiulier
document.addEventListener("DOMContentLoaded", function () {
  const checkboxes = document.querySelectorAll(".exclusive-checkbox");

  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", function () {
      if (this.checked) {
        checkboxes.forEach((cb) => {
          if (cb !== this) cb.checked = false;
        });
      }
    });
  });
});


//✅ description-produit

function changeImage(element) {
  document.getElementById("mainImage").src = element.src;
  document.querySelectorAll(".thumbnail").forEach(img => img.classList.remove("active"));
  element.classList.add("active");
}

function toggleInfo() {
  let content = document.getElementById("infoContent");
  if (content.classList.contains("expanded")) {
    content.classList.remove("expanded");
  } else {
    content.classList.add("expanded");
  }
}
