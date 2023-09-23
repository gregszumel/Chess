import { useState } from "react";

export interface Piece {
  type: string;
  player: number;
}

export interface GameState {
  pieces: Piece[][];
  player1Next: boolean;
}

export const initialPieces: Piece[][] = [
  [
    { type: "rook", player: 2 },
    { type: "pawn", player: 2 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "pawn", player: 1 },
    { type: "rook", player: 1 },
  ],
  [
    { type: "knight", player: 2 },
    { type: "pawn", player: 2 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "pawn", player: 1 },
    { type: "knight", player: 1 },
  ],
  [
    { type: "bishop", player: 2 },
    { type: "pawn", player: 2 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "pawn", player: 1 },
    { type: "bishop", player: 1 },
  ],
  [
    { type: "queen", player: 2 },
    { type: "pawn", player: 2 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "pawn", player: 1 },
    { type: "queen", player: 1 },
  ],
  [
    { type: "king", player: 2 },
    { type: "pawn", player: 2 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "pawn", player: 1 },
    { type: "king", player: 1 },
  ],
  [
    { type: "bishop", player: 2 },
    { type: "pawn", player: 2 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "pawn", player: 1 },
    { type: "bishop", player: 1 },
  ],
  [
    { type: "knight", player: 2 },
    { type: "pawn", player: 2 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "pawn", player: 1 },
    { type: "knight", player: 1 },
  ],
  [
    { type: "rook", player: 2 },
    { type: "pawn", player: 2 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "pawn", player: 1 },
    { type: "rook", player: 1 },
  ],
];

export function useGameState(): [Piece[][], boolean, Function] {
  const [pieces, setPieces] = useState(initialPieces);
  const [player1Next, setPlayer1Next] = useState(true);

  const makeMove = (fromX: number, fromY: number, toX: number, toY: number) => {
    if (!validMove(fromX, fromY, toX, toY)) {
      return;
    }
    var copiedPieces = copyPieces(pieces);
    const fromPiece = copiedPieces[fromX][fromY];
    console.log(fromX, fromY, toX, toY);
    console.log(fromPiece, copiedPieces[toX][toY]);
    copiedPieces[toX][toY] = { type: fromPiece.type, player: fromPiece.player };
    copiedPieces[fromX][fromY] = { type: "empty", player: -1 };
    console.log(copiedPieces[fromX][fromY], copiedPieces[toX][toY]);
    setPieces(copiedPieces);
    setPlayer1Next((prev) => !prev);
  };

  return [pieces, player1Next, makeMove];
}

function validMove(fromX: number, fromY: number, toX: number, toY: number) {
  return true;
}

function copyPieces(pieces: Piece[][]) {
  var copiedArray = [];
  for (var i = 0; i < 8; i++) {
    var pieceArray: Piece[] = [];
    copiedArray.push(pieceArray);
    for (var j = 0; j < 8; j++) {
      copiedArray[i].push(pieces[i][j]);
    }
  }
  return copiedArray;
}
