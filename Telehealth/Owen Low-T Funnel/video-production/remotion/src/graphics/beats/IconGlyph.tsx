import { Img, staticFile } from "remotion";

export type IconName =
  | "brain"
  | "factory"
  | "molecule"
  | "taxi"
  | "pituitary"
  | "lab-report"
  | "raw-material"
  | "valve"
  | "cortisol"
  | "testosterone";

export const IconGlyph: React.FC<{
  name: IconName;
  size?: number;
  style?: React.CSSProperties;
}> = ({ name, size = 120, style }) => {
  return (
    <Img
      src={staticFile(`icons/${name}.png`)}
      style={{
        width: size,
        height: size,
        objectFit: "contain",
        display: "block",
        ...style,
      }}
    />
  );
};
