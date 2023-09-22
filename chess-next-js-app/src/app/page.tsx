"use client";

import { useState, useEffect } from "react";
import knight from "./Chess_KnightDark.svg";

export default function Board() {
  const [knightCoordinates, setKnightCoordinates] = useState([0, 0]);

  function handleKnightMove([toX, toY]: [toX: number, toY: number]) {
    if (canMoveKnight([toX, toY])) {
      setKnightCoordinates([toX, toY]);
    }
  }
  function canMoveKnight([toX, toY]: [toX: number, toY: number]) {
    const [x, y] = knightCoordinates;
    const dx = toX - x;
    const dy = toY - y;

    return (
      (Math.abs(dx) === 2 && Math.abs(dy) === 1) ||
      (Math.abs(dx) === 1 && Math.abs(dy) === 2)
    );
  }

  const squares = [];
  for (var i = 0; i < 64; i++) {
    squares.push(
      <Square
        i={i}
        handleSquareClick={handleKnightMove}
        knightCoordinates={knightCoordinates}
      />
    );
  }

  return (
    <div className="h-96 w-96">
      <div className="grid h-full w-full auto-rows-fr grid-cols-8 grid-rows-8">
        {squares}
      </div>
    </div>
  );
}

function Square({
  i,
  knightCoordinates,
  handleSquareClick,
}: {
  i: number;
  knightCoordinates: number[];
  handleSquareClick: Function;
}) {
  const x = i % 8;
  const y = Math.floor(i / 8);
  const isKnightHere = x === knightCoordinates[0] && y === knightCoordinates[1];
  const black = (x + y) % 2 === 1;
  const piece = isKnightHere ? <Knight /> : null;
  const cn = black ? "bg-slate-500 " : "bg-slate-200 ";

  return (
    <div onClick={() => handleSquareClick([x, y])} className={cn}>
      {piece}
    </div>
  );
}

function Knight() {
  return (
    <img
      src={knight.src}
      onDragStart={(e) => {
        e.preventDefault();
      }}
    />
  );
}
