import { Component, OnInit } from '@angular/core';
import { BuildlistService } from './buildlist.service';
import { AppService } from '../app.service';

@Component({
  selector: 'app-buildlist',
  templateUrl: './buildlist.component.html',
  styleUrls: ['./buildlist.component.css']
})
export class BuildlistComponent implements OnInit {

  public data: object;
  public position = ['Home', 'Builds'];

  constructor(
    private _appService: AppService,
    private _service: BuildlistService
  ) { }

  ngOnInit() {
    this._service.getInfo().subscribe((resp: any) => {
      this.data = resp;
      console.log(this.data);
    });
  }

  status() { return this._appService.getLogin(); }
  id() { return this._appService.getId(); }

}
