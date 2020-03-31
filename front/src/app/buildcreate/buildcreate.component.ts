import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { AppService } from '../app.service';
import { v1 as uuid } from 'uuid';

@Component({
  selector: 'app-buildcreate',
  templateUrl: './buildcreate.component.html',
  styleUrls: ['./buildcreate.component.css']
})
export class BuildcreateComponent implements OnInit {

  public _buildForm: FormGroup;
  public _gemsForm: FormGroup;
  public _cubeForm: FormGroup;
  public _itemsForm: FormGroup;
  public _skillsForm: FormGroup;

  private uid: string;

  constructor(
    private _service: AppService,
    private _builder: FormBuilder
  ) {
    this.uid = uuid();
  }

  ngOnInit() {
    this._buildForm = this._builder.group({
      id: this.uid,
      name: ['', Validators.required],
      user: localStorage.getItem('id'),
      info: [''],
    });

    this._gemsForm = this._builder.group({
      id_build: this.uid,
      id_gem1: '',
      id_gem2: '',
      id_gem3: '',
    });

    this._cubeForm = this._builder.group({
      id_build: this.uid,
      id_item1: '',
      id_item2: '',
      id_item3: '',
    });

    this._itemsForm = this._builder.group({
      id_build: this.uid,
      id_item1: '',
      id_item2: '',
      id_item3: '',
      id_item4: '',
      id_item5: '',
      id_item6: '',
      id_item7: '',
      id_item8: '',
      id_item9: '',
      id_item10: '',
      id_item11: '',
      id_item12: '',
    });

    this._skillsForm = this._builder.group({
      id_build: this.uid,
      id_skill1: '',
      id_skill2: '',
      id_skill3: '',
      id_skill4: '',
      id_skill5: '',
      id_skill6: '',
      id_skill7: '',
      id_skill8: '',
      id_skill9: '',
      id_skill10: '',
    });
  }

  submit() {
    console.log('submited');
  }

}
