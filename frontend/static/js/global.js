// Función para formatear XML
function formatXML(xmlString) {
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(xmlString, "text/xml");
    const formattedXML = new XMLSerializer().serializeToString(xmlDoc.documentElement);
    return formattedXML;
  }