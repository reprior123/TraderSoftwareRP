 
    <div class="step">
            <div class="moduleTitle hd">
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} 5</h3>
                    <div class="clear"></div>
            </div>
            <div class="row portfolio-overview">
                    <div class="small-12 column">
                            <p><b>{$APP.LBL_COSTS_RELATIVE_ASSETS}</b><br><br>
                            </p>
                            <form class="step_form">
                                    <p>
    <input type="radio" name="costs_relative_assets" value="> 50% des Gesamtvermoegens" {if $data->costs_relative_assets eq "> 50% des Gesamtvermoegens"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_5_1_TEXT}<br>
    <input type="radio" name="costs_relative_assets" value="10% - 50% des Gesamtvermoegens" {if $data->costs_relative_assets eq "10% - 50% des Gesamtvermoegens"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_5_2_TEXT}<br>
    <input type="radio" name="costs_relative_assets" value="< 10%" {if $data->costs_relative_assets eq "< 10%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_5_3_TEXT}<br>
    <input type="radio" name="costs_relative_assets" value="nonfound" {if $data->costs_relative_assets eq "nonfound"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_5_4_TEXT}<br>
                                    </p>
                            </form>
                    </div>
            </div>
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="6" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>
    </div> 
