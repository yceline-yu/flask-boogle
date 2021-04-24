"use strict";

const $playedWords = $("#words");
const $form = $("#newWordForm");
const $wordInput = $("#wordInput");
const $message = $(".msg");
const $table = $("table");

let gameId;


/** Start */

async function start() {
  let response = await axios.get("/api/new-game");
  gameId = response.data.gameId;
  let board = response.data.board;

  displayBoard(board);
}

/** Display board */

function displayBoard(board) {
  // $table.empty();
  console.log("this is the board -> ", board)
  //loop over board and create the DOM tr/td structure
  //loop over board (array of arrays of single char string)
  //access the inner loop to append the char to a td in the table?
  //hei/wid should be same, outsideloop for hei, inner was for wid
  //outer loop only had one <tr>, inner had multiple <td> inner loop assigned the <td>insides
  //inner appended the tds to the tr
  //idk where the tr gets appened
  //$("tr td:nth-child(1)").text(array[0][0-4]) -> only gave back array(5)
  for (let letters of board){
    for (let i = 0; i < letters.length; i++){
      
    }
  }
}


start();

