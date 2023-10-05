function addRow(){
     let board = document.getElementById("game-board");

    for (let i = 0; i < NUMBER_OF_GUESSES; i++) {
        let row = document.createElement("div")
        row.className = "letter-row"

        for (let j = 0; j < 5; j++) {
            let box = document.createElement("div")
            box.className = "letter-box"
            box.onclick = function(){ applyColor(this);}
            row.appendChild(box)
        }
        board.appendChild(row)
    }
}

function initBoard() {
    addRow()
    // Color Boxes
    let board = document.getElementById("game-board");
    let row1 = document.createElement("div")
    row1.className = "letter-row"
    let box = document.createElement("div")
    box.className = "letter-box"
    box.style.backgroundColor = "green"
    box.onclick = function(){ setColor('green');}
    row1.appendChild(box)
    let box1 = document.createElement("div")
    box1.className = "letter-box"
    box1.style.backgroundColor = "yellow"
    box1.onclick = function(){ setColor('yellow');}
    row1.appendChild(box1)
    let box2 = document.createElement("div")
    box2.className = "letter-box"
    box2.style.backgroundColor = "white"
    box2.onclick = function(){ setColor('white');}
    row1.appendChild(box2)
    board.appendChild(row1)

}

function shadeKeyBoard(letter, color) {
    for (const elem of document.getElementsByClassName("keyboard-button")) {
        if (elem.textContent === letter) {
            let oldColor = elem.style.backgroundColor
            if (oldColor === 'green') {
                return
            }

            if (oldColor === 'yellow' && color !== 'green') {
                return
            }

            elem.style.backgroundColor = color
            break
        }
    }
}

const NUMBER_OF_GUESSES = 6;
let guessesRemaining = NUMBER_OF_GUESSES;
let currentGuess = [];
let colorsBox = [];
let nextLetter = 0;
let words_array = [];

document.addEventListener("keyup", (e) => {

    let pressedKey = String(e.key)
    if (pressedKey === "Backspace" && nextLetter !== 0) {
        deleteLetter()
        return
    }

    if (pressedKey === "Enter") {
        checkGuess()
        return
    }

    let found = pressedKey.match(/[a-z]/gi)
    if (!found || found.length > 1) {
        return
    } else {
        insertLetter(pressedKey)
    }
})


function insertLetter (pressedKey) {
    if (nextLetter === 5) {
        return
    }
    pressedKey = pressedKey.toLowerCase()

    let row = document.getElementsByClassName("letter-row")[6 - guessesRemaining]
    //let row = document.getElementsByClassName("letter-row")[0]
    let box = row.children[nextLetter]
    box.textContent = pressedKey
    box.classList.add("filled-box")
    currentGuess.push(pressedKey)
    nextLetter += 1
}
function deleteLetter () {
    let row = document.getElementsByClassName("letter-row")[6 - guessesRemaining]
    //let row = document.getElementsByClassName("letter-row")[0]
    let box = row.children[nextLetter - 1]
    box.textContent = ""
    box.classList.remove("filled-box")
    currentGuess.pop()
    nextLetter -= 1
}

function getData(){
    //let row = document.getElementsByClassName("letter-row")[0]
    let row = document.getElementsByClassName("letter-row")[6 - guessesRemaining]
    guessString = ''
    colorsBox =[]
    for (var i=0;i<5;i++)
    {

        if (row.children[i].style.backgroundColor  == 'green')
        {
            colorsBox.push('g')
        }
        else if (row.children[i].style.backgroundColor  == 'yellow')
        {
            colorsBox.push('y')
        }
        else
        {
            colorsBox.push('w')
        }
        guessString += row.children[i].textContent
    }
    return guessString
}

function checkGuess () {
    //console.log(currentGuess)
    let row = document.getElementsByClassName("letter-row")[6 - guessesRemaining]
    //let row = document.getElementsByClassName("letter-row")[0]
    let guessString = ''

    //let rightGuessString = 'train'
    //let rightGuess = Array.from(rightGuessString)
    guessString = getData()
    //for (const val of currentGuess) {
    //    guessString += val
    //}

    if (guessString.length != 5) {
        alert("Not enough letters!")
        return
    }

    //console.log(colorsBox)
    //if (!WORDS.includes(guessString)) {
    //    alert("Word not in list!")
    //    return
    //}
    var wordsArray = JSON.stringify(words_array)
    //wordsArray = JSON.stringiwords_array
    //console.log("guessstring")
    //console.log(guessString)
    //console.log("wordsArray")
    //console.log(wordsArray)

    fetch('solve/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ wordsArray, guessString,colorsBox })
           })
           .then(response => response.json())
        .then(responseData => {
            const next_guess = responseData.next_guess;
            const status = responseData.status;
            if (status =="fail"){
                alert("No words available")
                return
            }
            const words = responseData.words;
            // Populate the grid with the solved puzzle data
            //console.log(next_guess)
            //console.log(words)
            label_guess = document.getElementById("next-word")
            //console.log(label_guess)
            label_guess.innerHTML=next_guess
            label_words = document.getElementById("words")
            label_words.innerHTML=words
            words_array=words

            });



    //if (guessString === rightGuessString) {
    //    alert("You guessed right! Game over!")
    //    guessesRemaining = 0
    //    return
    //} else {
        guessesRemaining -= 1;
        currentGuess = [];
        nextLetter = 0;

    //    if (guessesRemaining === 0) {
    //        alert("You've run out of guesses! Game over!")
    //        alert(`The right word was: "${rightGuessString}"`)
    //    }

}

let selectedColor = null;

function setColor(color) {
    //console.log("hi")
    selectedColor = color;
}

function applyColor(box) {
    //console.log("hello")
    if (selectedColor) {
        box.style.backgroundColor = selectedColor;
    }
}

function refreshPage() {
    window.location.reload();
}

initBoard()