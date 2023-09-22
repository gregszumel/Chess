"use client";

import { ReactNode, useEffect, useState } from "react";
import knight from "./Chess_KnightDark.svg";
import { DndProvider, useDrag, useDrop } from "react-dnd";
import { HTML5Backend } from "react-dnd-html5-backend";

export default function Board() {
  const [knightCoordinates, setKnightCoordinates] = useState([0, 0]);
  useEffect(() => {
    console.log("use effect knight coordinates: ", knightCoordinates);
  });

  function handleKnightMove(toX: number, toY: number) {
    console.log(
      "handle knight move with ",
      toX,
      toY,
      "from",
      knightCoordinates
    );
    if (canMoveKnight(toX, toY)) {
      console.log("updating knight coordinates");
      setKnightCoordinates([toX, toY]);
    }
  }

  function canMoveKnight(toX: number, toY: number) {
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
      renderSquare(i, handleKnightMove, canMoveKnight, [
        knightCoordinates[0],
        knightCoordinates[1],
      ])
    );
  }

  return (
    <DndProvider backend={HTML5Backend}>
      <div className="h-96 w-96">
        <div
          className="grid h-full w-full auto-rows-fr grid-cols-8 grid-rows-8
       place-items-center"
        >
          {squares}
        </div>
      </div>
    </DndProvider>
  );
}

function renderSquare(
  i: number,
  handleKnightMove: Function,
  canMoveKnight: Function,
  [knightX, knightY]: [knightX: number, knightY: number]
) {
  const x = i % 8;
  const y = Math.floor(i / 8);
  return (
    <div key={i}>
      <BoardSquare
        x={x}
        y={y}
        knightX={knightX}
        knightY={knightY}
        moveKnight={handleKnightMove}
        canMoveKnight={canMoveKnight}
      >
        {renderPiece(x, y, [knightX, knightY])}
      </BoardSquare>
    </div>
  );
}

function renderPiece(
  x: number,
  y: number,
  [knightX, knightY]: [knightX: number, knightY: number]
) {
  if (x == knightX && y == knightY) {
    return <Knight x={x} y={y} />;
  }
}

function BoardSquare({
  x,
  y,
  knightX,
  knightY,
  moveKnight,
  canMoveKnight,
  children,
}: {
  x: number;
  y: number;
  knightX: number;
  knightY: number;
  moveKnight: Function;
  canMoveKnight: Function;
  children?: ReactNode;
}) {
  const black = (x + y) % 2 == 1;
  const [{ isOver, canDrop }, drop] = useDrop(
    () => ({
      accept: ItemTypes.KNIGHT,
      drop: () => moveKnight(x, y),
      canDrop: () => canMoveKnight(x, y),
      collect: (monitor) => ({
        isOver: !!monitor.isOver(),
        canDrop: !!monitor.canDrop(),
      }),
    }),
    [knightX, knightY]
  );

  const cn = isOver
    ? "absolute opacity-50 left-0 top-0 bg-black w-full h-full"
    : "";

  return (
    <div ref={drop} className="relative">
      <Square black={black}> {children} </Square>
      {isOver && !canDrop && <Overlay color="red" />}
      {isOver && canDrop && <Overlay color="green" />}
      {!isOver && canDrop && <Overlay color="yellow" />}
    </div>
  );
}

function Overlay({ color }: { color: string }) {
  return (
    <div
      style={{
        position: "absolute",
        top: 0,
        left: 0,
        height: "100%",
        width: "100%",
        opacity: 0.5,
        backgroundColor: color,
      }}
    />
  );
}

function Square({ black, children }: { black: boolean; children: ReactNode }) {
  const cn = black ? "bg-slate-500 h-12 w-12" : "bg-slate-200 h-12 w-12";
  return <div className={cn}> {children} </div>;
}

const ItemTypes = {
  KNIGHT: "knight",
};

function Knight({ x, y }: { x: number; y: number }) {
  const [{ isDragging }, drag] = useDrag(() => ({
    type: ItemTypes.KNIGHT,
    collect: (monitor) => ({
      isDragging: !!monitor.isDragging(),
    }),
  }));

  const cn = isDragging ? "opacity-50" : "opacity-100";

  return <img ref={drag} src={knight.src} className={cn} />;
}
