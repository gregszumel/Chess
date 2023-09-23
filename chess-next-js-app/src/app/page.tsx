"use client";

import { useState, ReactNode } from "react";
import {
  KD,
  QD,
  BD,
  ND,
  RD,
  PD,
  KL,
  QL,
  BL,
  NL,
  RL,
  PL,
} from "./Pieces/pieces";

interface Piece {
  type: string;
  player: number;
}

const initialPieces: Piece[][] = [
  [
    { type: "rook", player: 2 },
    { type: "knight", player: 2 },
    { type: "bishop", player: 2 },
    { type: "queen", player: 2 },
    { type: "king", player: 2 },
    { type: "bishop", player: 2 },
    { type: "knight", player: 2 },
    { type: "rook", player: 2 },
  ],
  [
    { type: "pawn", player: 2 },
    { type: "pawn", player: 2 },
    { type: "pawn", player: 2 },
    { type: "pawn", player: 2 },
    { type: "pawn", player: 2 },
    { type: "pawn", player: 2 },
    { type: "pawn", player: 2 },
    { type: "pawn", player: 2 },
  ],
  [
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
  ],
  [
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
  ],
  [
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
  ],
  [
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
    { type: "empty", player: -1 },
  ],
  [
    { type: "pawn", player: 1 },
    { type: "pawn", player: 1 },
    { type: "pawn", player: 1 },
    { type: "pawn", player: 1 },
    { type: "pawn", player: 1 },
    { type: "pawn", player: 1 },
    { type: "pawn", player: 1 },
    { type: "pawn", player: 1 },
  ],
  [
    { type: "rook", player: 1 },
    { type: "knight", player: 1 },
    { type: "bishop", player: 1 },
    { type: "queen", player: 1 },
    { type: "king", player: 1 },
    { type: "bishop", player: 1 },
    { type: "knight", player: 1 },
    { type: "rook", player: 1 },
  ],
];

function useGameState() {
  const [pieces, setPieces] = useState(initialPieces);
  const [player1Next, setPlayer1Next] = useState(true);

  const makeMove = (fromX: number, fromY: number, toX: number, toY: number) => {
    console.log(fromX, fromY, toX, toY);
    setPlayer1Next((prev) => !prev);
  };

  return [pieces, player1Next, makeMove];
}

export default function Home() {
  const squares = [];
  const [pieces, player1Next, setGameState] = useGameState();

  for (var i = 0; i < 64; i++) {
    squares.push(renderSquare(i, pieces));
  }

  return (
    <div className="w-96 h-96">
      <div className="grid place-items-center w-full h-full grid-cols-8 grid-rows-8">
        {squares}
      </div>
    </div>
  );
}

function renderSquare(i: number, pieces: any) {
  const x = i % 8;
  const y = Math.floor(i / 8);
  const black = (x + y) % 2 === 1;

  return (
    <div key={i}>
      <Square black={black}>{renderPiece(pieces[y][x])}</Square>
    </div>
  );
}

function renderPiece(piece: Piece) {
  function getPieceImg(piece: Piece) {
    if (piece.type == "king" && piece.player == 2) {
      return <KD />;
    } else if (piece.type == "queen" && piece.player == 2) {
      return <QD />;
    } else if (piece.type == "bishop" && piece.player == 2) {
      return <BD />;
    } else if (piece.type == "knight" && piece.player == 2) {
      return <ND />;
    } else if (piece.type == "rook" && piece.player == 2) {
      return <RD />;
    } else if (piece.type == "pawn" && piece.player == 2) {
      return <PD />;
    } else if (piece.type == "king" && piece.player == 1) {
      return <KL />;
    } else if (piece.type == "queen" && piece.player == 1) {
      return <QL />;
    } else if (piece.type == "bishop" && piece.player == 1) {
      return <BL />;
    } else if (piece.type == "knight" && piece.player == 1) {
      return <NL />;
    } else if (piece.type == "rook" && piece.player == 1) {
      return <RL />;
    } else if (piece.type == "pawn" && piece.player == 1) {
      return <PL />;
    }
    return "error";
  }
  return (
    <div className="w-full h-full flex items-center justify-center">
      {piece.type != "empty" && getPieceImg(piece)}
    </div>
  );
}

function Square({ black, children }: { black: boolean; children: ReactNode }) {
  const cn = black ? "bg-slate-500 h-12 w-12" : "bg-slate-200 h-12 w-12";

  return <div className={cn}> {children} </div>;
}
