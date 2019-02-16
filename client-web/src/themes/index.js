import WebFont from 'webfontloader';
import { library, dom } from "@fortawesome/fontawesome-svg-core";
import { faBars } from "@fortawesome/free-solid-svg-icons/faBars";
import { faEdit } from "@fortawesome/free-solid-svg-icons/faEdit";
import { faList } from "@fortawesome/free-solid-svg-icons/faList";
import { faPlus } from "@fortawesome/free-solid-svg-icons/faPlus";
import { faTrashAlt } from "@fortawesome/free-solid-svg-icons/faTrashAlt";

import 'bootstrap-css-only/css/bootstrap.min.css';

import './base';

WebFont.load({
  google: {
    families: ['Lato', 'Nunito', 'sans-serif']
  }
});

library.add(faBars);
library.add(faEdit);
library.add(faList);
library.add(faPlus);
library.add(faTrashAlt);
dom.watch();
