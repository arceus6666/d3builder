import { Component } from '@angular/core';
import { AppService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'front';

  constructor(
    private _service: AppService
  ) {
    this._service.init();
  }

  status() { return this._service.getLogin(); }
  id() { return this._service.getId(); }
}
