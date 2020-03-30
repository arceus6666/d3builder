import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  private _login = false;
  private _id: string = null;

  constructor() { }

  init() {
    const id = localStorage.getItem('id');
    if (id) {
      this.setId(id);
      this.setLogin(true);
    }
  }

  setLogin(status: boolean): void { this._login = status; }
  getLogin(): boolean { return this._login; }
  setId(id: string): void { this._id = id; }
  getId(): string { return this._id; }
}
