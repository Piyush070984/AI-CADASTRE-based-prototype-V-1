/// <reference types="vite/client" />

declare module '*.geojson' {
  const value: import('geojson').GeoJsonObject
  export default value
}
