const switchTheme = document.getElementById('switch')
const test = document.getElementById('switch-week')
const test1 = document.getElementById('mid')
const test2 = document.getElementById('mid-second')
let styleSheetType = document.documentElement

function applyThemeFromLocalStorage() {
    const savedTheme = localStorage.getItem('theme')
    const savedClass = localStorage.getItem('class')
    if (savedTheme) {
        styleSheetType.setAttribute('id', savedTheme)
        switchTheme.setAttribute('class', savedClass)
    }
}

function saveThemeToLocalStorage(mainTheme, mainClass) {
    localStorage.setItem('theme', mainTheme)
    localStorage.setItem('class', mainClass)
}

switchTheme.onclick = function() {
    if (styleSheetType.id === 'light') {
            this.classList.add('switch-on')
            styleSheetType.setAttribute('id', 'dark')
            saveThemeToLocalStorage('dark', this.classList.value)
    } else {
            this.classList.remove('switch-on')
            styleSheetType.setAttribute('id', 'light')
            saveThemeToLocalStorage('light', this.classList.value)
    }
}

applyThemeFromLocalStorage();

test.onclick = function() {
    if (test1.style.display == 'grid') {
        test1.style.display = 'none'
        test2.style.display = 'grid'
    } else {
        test2.style.display = 'none'
        test1.style.display = 'grid'
    }

}