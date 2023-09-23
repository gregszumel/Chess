"use client";

import { useState, ReactNode } from "react";
import { Piece, useGameState } from "./game";
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

export default function Home() {
  const squares = [];
  const [pieces, player1Next, nextMove] = useGameState();
  const [selectedPiece, setSelectedPiece] = useState(null);

  for (var i = 0; i < 64; i++) {
    squares.push(
      renderSquare(
        i,
        pieces,
        player1Next,
        nextMove,
        selectedPiece,
        setSelectedPiece
      )
    );
  }

  return (
    <div>
      <div className="text-sm">
        {player1Next ? "Player 1's turn" : "Player 2's turn"}
      </div>
      <div className="w-96 h-96">
        <div className="grid place-items-center w-full h-full grid-cols-8 grid-rows-8">
          {squares}
        </div>
      </div>
    </div>
  );
}

function renderSquare(
  i: number,
  pieces: Piece[][],
  player1Next: boolean,
  nextMove: Function,
  selectedPiece: number[] | null,
  setSelectedPiece: Function
) {
  const x = i % 8;
  const y = Math.floor(i / 8);
  const black = (x + y) % 2 === 1;
  const piece = pieces[x][y];
  const currPlayersPiece = (piece.player == 1) == player1Next;

  function handleSquareClick() {
    // set/change selectedPiece
    // TODO: don't allow jump overs
    if (piece.type != "empty" && currPlayersPiece) {
      setSelectedPiece([x, y]);
    } else if (selectedPiece && (piece.type == "empty" || !currPlayersPiece)) {
      console.log("move!");
      nextMove(selectedPiece[0], selectedPiece[1], x, y);
      setSelectedPiece(null);
    }
  }

  return (
    <div key={i} className="relative" onClick={handleSquareClick}>
      <Square black={black}>{renderPiece(piece)}</Square>
      {selectedPiece && selectedPiece[0] == x && selectedPiece[1] == y && (
        <div
          className="absolute left-0 top-0 h-full w-full opacity-50 
      bg-yellow-800"
        />
      )}
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
