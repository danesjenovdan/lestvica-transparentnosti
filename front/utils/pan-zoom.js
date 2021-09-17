/**
 * Based on: https://github.com/andi23rosca/vue-pan-zoom
 */

class Point {
  constructor(x = 0, y = 0) {
    this.x = x;
    this.y = y;
  }

  add(p) {
    return new Point(this.x + p.x, this.y + p.y);
  }

  subtract(p) {
    return new Point(this.x - p.x, this.y - p.y);
  }

  clone() {
    return new Point(this.x, this.y);
  }

  distanceTo(p) {
    return Math.hypot(this.x - p.x, this.y - p.y);
  }

  centerTo(p) {
    return new Point((this.x + p.x) / 2, (this.y + p.y) / 2);
  }
}

const touchPoint = (e, finger) =>
  new Point(e.touches[finger].clientX, e.touches[finger].clientY);
const mousePoint = (e) => new Point(e.clientX, e.clientY);

export default function panZoom({
  container,
  content,
  minZoom = 0.9,
  maxZoom = 15,
  zoomStep = 0.2,
  onReady = () => {},
  onTransformChange = () => {},
}) {
  container.style.cursor = 'grab';
  let panning = false;
  let zooming = false;
  let start0 = new Point();
  let end0 = new Point();
  let startDist = 0;
  let endDist = 0;
  let zoom = 1;
  let lastZoom = 1;
  let scaledSize = 0;

  let disableClick = false;
  let end0OnMouseDown = new Point();

  function setTransform(point, scale) {
    end0 = new Point(point.x, point.y);
    zoom = scale;
    content.style.transform = `translate(${point.x}px, ${point.y}px) scale(${scale})`;
    onTransformChange({ x: point.x, y: point.y }, scale);
  }

  function setZoom(z) {
    zoom = z = Math.max(Math.min(z, maxZoom), minZoom);
  }

  function touchMove(e) {
    if (panning) {
      end0 = touchPoint(e, 0).subtract(start0);
      setTransform(end0, zoom);
    } else if (zooming) {
      const finger0 = touchPoint(e, 0);
      const finger1 = touchPoint(e, 1);
      end0 = finger0.centerTo(finger1).subtract(start0);
      endDist = finger0.distanceTo(finger1) * lastZoom - startDist;
      const hd = endDist + scaledSize;
      setZoom(lastZoom * (hd / scaledSize) ** 4);
      setTransform(end0, zoom);
    }
    e.preventDefault();
  }

  function touchEnd(e) {
    zooming = false;
    if (e.touches.length === 1) {
      panning = true;
      start0 = touchPoint(e, 0).subtract(end0);
    } else {
      panning = false;
      window.removeEventListener('touchmove', touchMove);
      window.removeEventListener('touchend', touchEnd);
    }
    e.preventDefault();
  }

  function touchStart(e) {
    if (e.touches.length === 1) {
      panning = true;
      zooming = false;
      start0 = touchPoint(e, 0).subtract(end0);
    } else if (e.touches.length === 2) {
      zooming = true;
      panning = false;
      const finger0 = touchPoint(e, 0);
      const finger1 = touchPoint(e, 1);
      start0 = finger0.centerTo(finger1).subtract(end0);
      lastZoom = zoom;
      scaledSize =
        Math.hypot(content.offsetWidth, content.offsetHeight) * lastZoom;
      startDist = finger0.distanceTo(finger1) * lastZoom;
    }
    window.addEventListener('touchmove', touchMove);
    window.addEventListener('touchend', touchEnd);
    e.preventDefault();
  }

  function mouseMove(e) {
    const distance = start0.distanceTo(mousePoint(e).subtract(end0OnMouseDown));
    if (distance >= 4) {
      disableClick = true;
    }
    if (panning) {
      end0 = mousePoint(e).subtract(start0);
      setTransform(end0, zoom);
    }
  }

  function mouseUp() {
    container.style.cursor = 'grab';
    panning = false;
    window.removeEventListener('mousemove', mouseMove);
    window.removeEventListener('mouseup', mouseUp);
  }

  function mouseDown(e) {
    panning = true;
    disableClick = false;
    container.style.cursor = 'grabbing';
    start0 = mousePoint(e).subtract(end0);
    end0OnMouseDown = end0.clone();
    window.addEventListener('mousemove', mouseMove);
    window.addEventListener('mouseup', mouseUp);
    e.preventDefault();
  }

  function mouseWheel(e) {
    if (e.deltaY > 0) {
      setZoom(zoom * 2 ** -zoomStep);
    } else if (e.deltaY < 0) {
      setZoom(zoom * 2 ** zoomStep);
    }
    setTransform(end0, zoom);
    e.preventDefault();
  }

  function mouseClick(e) {
    if (disableClick) {
      e.preventDefault();
      e.stopPropagation();
      e.stopImmediatePropagation();
    }
  }

  container.addEventListener('touchstart', touchStart);
  container.addEventListener('mousedown', mouseDown);
  container.addEventListener('wheel', mouseWheel);
  container.addEventListener('contextmenu', (e) => e.preventDefault());
  container.addEventListener('click', mouseClick, true);

  onReady({
    setTransform,
    disable() {
      container.removeEventListener('touchstart', touchStart);
      container.removeEventListener('mousedown', mouseDown);
      container.removeEventListener('wheel', mouseWheel);
      container.removeEventListener('click', mouseClick, true);
      container.style.cursor = '';
    },
  });
}
